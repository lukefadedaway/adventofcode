//
//  main.swift
//  AdventOfCode
//
//  Created by Lukas Görtz on 21.12.22.
//

import Foundation

enum States: CaseIterable {
    case Number, Add, Sub, Mult, Div
}

precedencegroup PowerPrecedence { higherThan: MultiplicationPrecedence }
infix operator ^^ : PowerPrecedence
func ^^ (radix: Int, power: Int) -> Int {
    return Int(pow(Double(radix), Double(power)))
}

class monkey {
    var state: States
    var content: String
    
    init(state: States, content: String) {
        self.state = state
        self.content = content
    }
    // Needs Double precision for Part 2, otherwise off by 1
    public var getNumber: Double {
        switch state {
            case .Number:
                return Double(content)!
            case .Add:
                let parts = content.components(separatedBy: " + ")
                return (monkeylist[parts[0]]!.getNumber + monkeylist[parts[1]]!.getNumber)
            case .Sub:
                let parts = content.components(separatedBy: " - ")
                return (monkeylist[parts[0]]!.getNumber - monkeylist[parts[1]]!.getNumber)
            case .Mult:
                let parts = content.components(separatedBy: " * ")
                return (monkeylist[parts[0]]!.getNumber * monkeylist[parts[1]]!.getNumber)
            case .Div:
                let parts = content.components(separatedBy: " / ")
                return (monkeylist[parts[0]]!.getNumber / monkeylist[parts[1]]!.getNumber)
        }
    }
    public var getParts: [String] {
        switch state {
            case .Number:
                return []
            case .Add:
                return content.components(separatedBy: " + ")
            case .Sub:
                return content.components(separatedBy: " - ")
            case .Mult:
                return content.components(separatedBy: " * ")
            case .Div:
                return content.components(separatedBy: " / ")
        }
    }
}

var monkeylist: [String:monkey] = [:]

var getInput: String {
    if let st = readLine() {
        return st
    } else {
        return ""
    }
}

var input: String = getInput
while(input != "") {
    let parts = input.components(separatedBy: ": ")
    var monktype: States {
        if parts[1].contains("+") {
            return .Add
        }
        if parts[1].contains("-") {
            return .Sub
        }
        if parts[1].contains("*") {
            return .Mult
        }
        if parts[1].contains("/") {
            return .Div
        }
        return .Number
    }
    monkeylist[parts[0]] = monkey(state: monktype, content: parts[1])
    input = getInput
}
print("Part 1:\n\(Int(monkeylist["root"]!.getNumber))")

var rootParts = monkeylist["root"]!.getParts

func containsHumn(part: String) -> Bool {
    if(part.contains("humn")) {
        return true
    }
    if(monkeylist[part]!.state == .Number) {
        return false
    }
    let newparts = monkeylist[part]!.getParts
    return (containsHumn(part: newparts[0])) || (containsHumn(part: newparts[1]))
}
var whohashumn = [containsHumn(part: rootParts[0]),containsHumn(part: rootParts[1])]
monkeylist["humn"]!.state = .Number
if(whohashumn[0]) {
    var L = 0
    var R = 10000000000000
    monkeylist["humn"]!.content = "10000000000000"
    let tosearch = monkeylist[rootParts[1]]!.getNumber
    while(L <= R) {
        let m = Int((L+R)/2)
        monkeylist["humn"]!.content = String(m)
        if(tosearch < monkeylist[rootParts[0]]!.getNumber) {
            L = m + 1
            continue
        }
        if(tosearch > monkeylist[rootParts[0]]!.getNumber) {
            R = m - 1
            continue
        }
        break
    }
    print("Part 2:\n\(Int(monkeylist["humn"]!.getNumber))")
}
if(whohashumn[1]) {
    var L = 0
    var R = 100000000000000
    monkeylist["humn"]!.content = "100000000000000"
    let tosearch = monkeylist[rootParts[0]]!.getNumber
    while(L <= R) {
        let m = Int((L+R)/2)
        monkeylist["humn"]!.content = String(m)
        if(tosearch < monkeylist[rootParts[1]]!.getNumber) {
            L = m + 1
            continue
        }
        if(tosearch > monkeylist[rootParts[1]]!.getNumber) {
            R = m - 1
            continue
        }
        break
    }
    print("Part 2:\n\(Int(monkeylist["humn"]!.getNumber))")
}
