var list_val = ["",'CC','50-50','OC']
var count = 0;

function createDiv(to_set_cls_name){
  var IDiv = document.createElement('div');
  IDiv.className = to_set_cls_name;
  return IDiv;
}

function createSelect(list_of_options, elem_name){
  var option_count = 0;
  var newSelect = document.createElement('select');
  newSelect.name = elem_name;
  for(var options of list_of_options){
    var newOption = document.createElement("option");
    newOption.text = options;
    newOption.value = options;
    if(options === ""){
      newOption.disabled = true;
      newOption.hidden = true;
      newOption.selected= true;
    }
    newSelect.add(newOption);
    option_count += 1;
  }
  return newSelect;
}

function createTextArea(elem_name){
  var newTextArea = document.createElement("TEXTAREA");
  newTextArea.rows = 3;
  newTextArea.name = elem_name;
  return newTextArea;
}

function addChoice(){
  var newDiv = createDiv("row");
  newDiv.id = "choices-wrapper" + count.toString();

  var newColDiv_1 = createDiv("column-1");
  newColDiv_1.id = "choice-type-"+count.toString();
  newColDiv_1.appendChild(createSelect(list_val, "choice-type-"+count.toString()));

  var newColDiv_2 = createDiv("column-2");
  newColDiv_2.id = "choice-value-"+count.toString();
  newColDiv_2.appendChild(createTextArea("choice-value-"+count.toString()));

  newDiv.appendChild(newColDiv_1);
  newDiv.appendChild(newColDiv_2);

  count += 1;
  document.getElementById("choice-wrapper-id").appendChild(newDiv);
}