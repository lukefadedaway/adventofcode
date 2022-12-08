//
//  main.swift
//  AdventOfCode
//
//  Created by Lukas Görtz on 07.12.22.
//

import Foundation

class dir {
    public var dirs: [String:dir] = [:]
    public var files: [String:Int] = [:]
    public var parentdir: dir?
    
    init(parentdir: dir? = nil) {
        self.parentdir = parentdir
    }
    
    public func insertDir(name: String, directory: dir) {
        if(self.dirs[name] == nil) {
            self.dirs[name] = directory
            self.dirs[name]?.parentdir = self
        }
    }
    
    public func insertFile(name: String, value: Int) {
        if(self.files[name] == nil) {
            self.files[name] = value
        }
    }
    
    public var dirsize: Int {
        var size = 0
        for x in self.files.values {
            size += x
        }
        for x in self.dirs.values {
            size += x.dirsize
        }
        return size
    }
}

var basedir = dir()
var currentdir = basedir

var getInput: String {
    if let st = readLine() {
        return st
    } else {
        return ""
    }
}

var s = getInput // Skip cd /
s = getInput
while (s != "") {
    if(s.starts(with: "$ ")) {
        let parts = s.components(separatedBy: " ")
        if(parts[1] == "cd") {
            if(parts[2] == "..") {
                currentdir = currentdir.parentdir!
            } else {
                currentdir = currentdir.dirs[parts[2]]!
            }
        }
    } else {
        let parts = s.components(separatedBy: " ")
        if(parts[0] == "dir") {
            currentdir.insertDir(name: parts[1], directory: dir())
        } else {
            currentdir.insertFile(name: parts[1], value: Int(parts[0]) ?? 0)
        }
    }
    s = getInput
}

currentdir = basedir

func maxsumPart1(directory: dir) -> Int {
    var sum = 0
    if(directory.dirsize <= 100000) {
        sum += directory.dirsize
    }
    for x in directory.dirs.values {
        sum += maxsumPart1(directory: x)
    }
    return sum
}
var summe = maxsumPart1(directory: currentdir)
print("Part 1:")
print(summe)

var neededSpace = 30000000 - (70000000 - basedir.dirsize)
var candidates = [70000000]
currentdir = basedir
func minDirPart2(directory: dir) {
    if(directory.dirsize >= neededSpace) {
        candidates.append(directory.dirsize)
        for x in directory.dirs.values {
            minDirPart2(directory: x)
        }
    }
}
minDirPart2(directory: currentdir)
print("Part 2:")
print(candidates.min()!)
