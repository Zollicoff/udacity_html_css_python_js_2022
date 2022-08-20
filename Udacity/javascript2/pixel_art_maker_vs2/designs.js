// global variables for query selectors
const sizePickerVar = document.querySelector('#sizePicker [type="submit"]');
const pixelCanvasVar = document.querySelector("#pixelCanvas");
const colorPickerVar = document.querySelector("#colorPicker");
// function to make grid based on input and submit
function makeGrid() {
  pixelCanvas.innerHTML = '';
  var height = document.querySelector("#inputHeight").value;
  var width = document.querySelector("#inputWidth").value;
  for (var row = 0; row < height; row++) {
    tr = document.createElement("tr");
    for (var cell = 0; cell < width; cell++) {
      td = document.createElement("td");
      tr.insertAdjacentElement("afterbegin",td)
    }
    pixelCanvasVar.insertAdjacentElement("afterbegin",tr)
  }
}
// part of grid creation
sizePickerVar.addEventListener("click", function (event) {
  event.preventDefault();
});
sizePickerVar.addEventListener("click", makeGrid);
// function for color picker
pixelCanvasVar.addEventListener("click", function (event) {
  if (event.target.tagName === "TD") {
    var colval = document.querySelector("#colorPicker").value;
    event.target.style.backgroundColor = colval;
  }
});
