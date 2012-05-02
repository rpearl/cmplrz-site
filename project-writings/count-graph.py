#!/usr/bin/env python

import sys
from scipy.stats import stats
import Gnuplot, Gnuplot.funcutils

measurements = ["Add"]

def process_file(file_name):
    bs, name, mode, suite = file_name.split("_")
    name = name.replace("check-", "")
    name = name.replace("run-", "")
    suite = "test" # HACK
    lines = [line.strip() for line in open(file_name)]
    counts = {}
    for s in measurements:
        total, finite, truncated, both = 0, 0, 0, 0
        for line in lines:
            if s in line:
                _, _, is_finite, is_truncated = line.split(" ")
                is_finite, is_truncated = int(is_finite), int(is_truncated)
                if is_finite: finite += 1
                if is_truncated: truncated += 1
                if is_finite and is_truncated: both += 1
                total += 1
        counts[s] = (total, finite, truncated, both)
                
    return (name, suite, mode, counts)

def map_add(m, key, x):
    if key not in m:
        m[key] = []
    m[key].append(x)

def organize_data(data, suite):
    data = [x[:1]+x[2:] for x in data if x[1] == suite]
    modes = {(x[1], y): [] for x in data for y in measurements}
    for x in data:
        for k, v in x[2].iteritems():
            #if v[0] == 0: v = 1
            #else: v = float(v[1])/float(v[0])
            modes[(x[1], k)].append((x[0], (v[0], v[1])))
    for v in modes.values():
        v.sort()
    return modes

def reorganize_data(data, suite):
    modes = list(data.keys())
    data2 = {}
    for k, v in data.iteritems():
        for (test, entry) in v:
            map_add(data2, test, entry)
    return (modes, data2)

def produce_stats(data):
    m = {}
    for (server, size, conns, it, time, rate) in data:
        map_add(m, (server, size, conns), rate)
    data = []
    for k, v in m.items():
        mean = stats.nanmean(v)
        stddev = stats.nanstd(v)
        data += [k + (mean, stddev)]
    return data

def spew_data(suite, table):
    modes, table = table
    f = open(suite + "_counts.csv", "w")
    i = 0
    for test, points in table.iteritems():
        if all(x[0] < 5 for x in points): continue
        f.write(test + ',')
        butt = []
        for (total, removed) in points:
            if total == 0: v = 0
            else: v = float(removed)/float(total)
            butt += [str(v)]
        f.write(",".join(butt))
        f.write("\n")
    f.close()

def graph(size, table):
    g = Gnuplot.Gnuplot(debug=1)
    #g.title(size)
    g('set style data histograms')
    g('set yrange [0:]')
    g('set style fill solid border -1')
#    g('set key autotitle columnheader')
    #g('set xrange [0:525]') # XXX: change if we change max conns
    g.xlabel('Test name')
    g.ylabel('% overflow checks eliminated')

    lines = []
    for key, data in sorted(table.items()):
        mode, add = key
        xs, ys = zip(*data)
        xs = range(len(xs))
        lines.append(Gnuplot.Data(ys, title=mode + " " + add))
    g.itemlist = lines

    g.hardcopy('graph_' + size + '.ps', enhanced=1, color=1)


def main(args):
    data = [process_file(f) for f in args[1:]]
    #print data

    #data = produce_stats(data)

    suites = set(x[1] for x in data)

    tables = {suite: reorganize_data(organize_data(data, suite), suite) for suite in suites}

    for suite, table in tables.items():
        spew_data(suite, table)
        #graph(suite, table)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
