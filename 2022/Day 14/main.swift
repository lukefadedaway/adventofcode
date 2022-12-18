//
//  main.swift
//  AdventOfCode
//
//  Created by Lukas Görtz on 14.12.22.
//

import Foundation

enum States: String, CaseIterable {
    case Air = "."
    case Rock = "#"
    case Sand = "o"
}

var getInput: String {
    if let st = readLine() {
        return st
    } else {
        return ""
    }
}

var lines: [[(Int,Int)]] = []
var minx = 1000000, miny = 1000000, maxx = -1000000, maxy = -1000000
var input: String = getInput
while(input != "") {
    let line_ = input.replacingOccurrences(of: " -> ", with: ",").components(separatedBy: ",")
    let line = stride(from: 0, to: line_.count - 1, by: 2).map {
        (Int(line_[$0])!, Int(line_[$0+1])!)
    }
    for l in line {
        minx = min(minx,l.0)
        maxx = max(maxx,l.0)
        miny = min(miny,l.1)
        maxy = max(maxy,l.1)
    }
    input = getInput
    lines.append(line)
}
var playarea = Array(repeating: Array(repeating: States.Air, count: 500+maxy+10), count: maxy+3)
for x in lines {
    for y in 1..<x.count {
        let x1 = x[y-1].0
        let x2 = x[y].0
        let y1 = x[y-1].1
        let y2 = x[y].1
        if(x1 == x2) {
            for z in min(y1,y2)..<max(y1,y2)+1 {
                playarea[z][x1] = .Rock
            }
        }
        if(y1 == y2) {
            for z in min(x1,x2)..<max(x1,x2)+1 {
                playarea[y1][z] = .Rock
            }
        }
    }
}
for x in 0..<playarea[playarea.count-1].count {
    playarea[playarea.count-1][x] = .Rock
}
var rounds = 0
var inPart1 = true

while (playarea[0][500] != .Sand) {
    rounds += 1
    var curpos = (0,500) // y,x
    while true {
        if(playarea[curpos.0 + 1][curpos.1] != .Air) {
            if(playarea[curpos.0 + 1][curpos.1 - 1] != .Air) {
                if(playarea[curpos.0 + 1][curpos.1 + 1] != .Air) {
                    playarea[curpos.0][curpos.1] = .Sand
                    break
                }
                curpos = (curpos.0 + 1, curpos.1 + 1)
                continue
            }
            curpos = (curpos.0 + 1, curpos.1 - 1)
            continue
        }
        curpos = (curpos.0 + 1, curpos.1)
    }
    if curpos.0 > maxy && inPart1{
        inPart1 = false
        print("Part 1:\n\(rounds-1)")
    }
}
print("Part 2:\n\(rounds)")

//for x in playarea {
//    var s = ""
//    for y in x {
//        s += y.rawValue
//    }
//    print(s)
//}
