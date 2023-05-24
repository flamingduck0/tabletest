var rIndex, cIndex, savedRow, savedCol;
table = document.getElementById("table");


function clickedCell() {
    for(let i = 0; i < table.rows.length; i++) {
        for(let j = 0; j < table.rows[i].cells.length; j++) {

            //hovering pair indicator
            table.rows[i].cells[j].onmouseover = function () {

                //update values for cIndex and rIndex
                cIndex = this.cellIndex;
                rIndex = this.parentElement.rowIndex;

                //hover indicating done in js instead of css to do dual hovering
                //Remove all old hover indicator from the previous cell
                for (let highlights = 0; highlights <= document.querySelectorAll('.hover')?.length; highlights ++) {
                    document.querySelector('.hover')?.classList.remove('hover');
                    //thanks Comben!
                }

                //adds hover effect
                if(!(this.classList.contains("head") || this.classList.contains("invis"))) {
                    this.classList.add('hover');
                    try {
                        table.rows[cIndex].cells[rIndex].classList.add('hover');
                    } catch (error) {
                        console.error(error)
                    }
                }
            }
        }
    }
}
clickedCell();

table.onclick = function() {
    if (cIndex>0 && rIndex>0 && cIndex!=rIndex) {

        // Remove all highlight from the previous cell
        for (let highlights = 0; highlights <= document.querySelectorAll('.highlight')?.length; highlights ++) {
            document.querySelector('.highlight')?.classList.remove('highlight', 'selected');
            //thanks Comben!
        }

        // Add highlight to the clicked cell
        table.rows[rIndex].cells[cIndex].classList.add('highlight');
        table.rows[rIndex].cells[cIndex].classList.add('selected');
        try {
            table.rows[cIndex].cells[rIndex].classList.add('highlight');
        } catch (error) {
            console.error(error)
        }

        //save these values not cIndex and rIndex as they change when clicking row and col headers
        savedCol = cIndex;
        savedRow = rIndex;

        console.log(savedCol, savedRow);
        console.log(fencers[savedRow-1]+" vs "+fencers[savedCol-1])
    }
}