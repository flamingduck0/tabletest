table = document.getElementById("table");

console.log(fencers)
console.log(tableList)

//make the heading row
let headRow = document.createElement("tr");

//first invisible header element
let empty = document.createElement("th");
empty.classList.add('invis')

headRow.append(empty)
//make a heading element per user
for(let i = 0; i < fencers.length; i++) {
    let tableHeader = document.createElement("th")
    tableHeader.innerText = fencers[i]
    tableHeader.classList.add("head")
    headRow.append(tableHeader)
}

table.append(headRow)

//make each row

for(let i = 0; i < fencers.length; i++) {
    let row = document.createElement("tr");
    let cHead = document.createElement("td");
    cHead.classList.add('head')
    cHead.innerText = fencers[i]
    row.append(cHead)
    for(let j = 0; j < fencers.length; j++) {
        let value = document.createElement("td")
        if(i == j) {
            value.classList.add("invis")
            //insert clever function here
        }
        value.innerText = tableList[i][j]
        row.append(value)
    }
    table.append(row)
}



