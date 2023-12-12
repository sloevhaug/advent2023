const fs = require('fs');
const readline = require('readline');
const math = require('mathjs');

const fileStream = fs.createReadStream('8-input.txt');

const path = "LRLRRRLRRRLLLRLRRLLRLRRRLRLRRRLRLRRRLRLRRRLRRRLRLLRRRLRLRLRRLRRLRLRRLRRLRRLLRRRLRRRLRRLRRLRRLRRRLLRRLRLRRLRLRRLRRLRLRRLRRLLRLRRRLRRLRRRLLRLRLRLLRLLRLLRLRRLLRRLRLRLRRLRLLRRRLLRRRLRRLLRRRLRRRLRLRRRLLRRRLRLRRRLLLRRRLRLRLRRRLRRRLRRRLRLRRLLLRRLRRRLLRLRRRLRLRLLLRRLRLRRRLRLRRRR";
const start = "AAA";
let starters = [];
let allSteps = [];
let pos = 0;

const rl = readline.createInterface({
  input: fileStream,
  crlfDelay: Infinity
});

let dictionary = {};

const findPath = () => {
    
    let next = start;
    let steps = 1;
    
    while(true){
        
        //console.log("Next: ", next, " dictionary: ", dictionary[next], " direction: ", path[pos], " pos: ", pos, " steps: ", steps)
        
        if(path[pos] == 'L'){
            next = dictionary[next][0]
        }else{
            next = dictionary[next][1]
        }
        
        if(next === 'ZZZ'){
            console.log("Part one steps: ", steps)
            break;
        }
        
        steps ++;
        pos ++;
        
        if(pos === path.length) pos = 0;
        
    }
}

const findPath2 = (start) => {

    let next = start;
    let steps = 1;
    let pos = 0;
    
    while(true){

        if(path[pos] == 'L'){
            next = dictionary[next][0]
        }else{
            next = dictionary[next][1]
        }

        if(next.endsWith("Z")){
            allSteps.push(steps)
            break;
        }

        steps ++;
        pos ++;

        if(pos === path.length) pos = 0;

    }
}


rl.on('line', (line) => {
    let test = line.split('=');
    let noekkel = test[0].trim()
    let verdi = test[1].trim()
    .replace("(", "")
    .replace(")", "")
    .split(", ")
    dictionary[noekkel] = verdi;
    if(noekkel.endsWith("A")){
        starters.push(noekkel)
    }
});

rl.on('close', () => {
    
    findPath()
    
    console.log("Starters part 2: ", starters)
    starters.forEach((start) => {
        findPath2(start)
    })
    
    console.log("Part 2 total steps: ", math.lcm(...allSteps))
});

