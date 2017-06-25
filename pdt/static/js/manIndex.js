function reportButton(name, stime, etime, delta, inter, esize, asize, eeffort, aeffort, per){
  //scrptE.setAttribute("src", "button.js?" + (Date.now() % 10000));
  var text = "";
  text += "<div class=\"modal fade\" id=\"reportModal"+name+"\" tabindex=\"-1\" role=\"dialog\" aria-labelledby=\"reportModalLabel\">";
  text += "<div class=\"modal-dialog\" role=\"document\">";
  text += "<div class=\"modal-content\">";
  text += "<div class=\"modal-header\">";
  text += "<button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>";
  text += "<h4 class=\"modal-title\">Metrics</h4></div>";
  
  // modal body
  text += "<div class=\"modal-body\">";
  text += "<div class='row'><div class='col-md-12'>";
  text += "<div class='panel panel-default'><div class='panel-body'>";
  text += "<div class='bs-example bs-example-tabs' data-example-id='togglable-tabs'>";
  text += "<ul id='myTabs' class='nav nav-tabs' role='tab-list'>";
  text += "<li role='presentation' class='active'><a href='#time' id='time-tab' role='tab' data-toggle='tab' aria-controls=\"time\" aria-expanded=\"true\">Time</a></li>";

  text += "<li role='presentation'><a href='#size' role='tab' id='size-tab' data-toggle='tab' aria-controls='size'>Size</a></li>";
  text += "<li role=\"presentation\"><a href=\"#defect\" role=\"tab\" id=\"efect-tab\" data-toggle=\"tab\" aria-controls=\"efect\">Defect</a></li></ul>";
  // time
  text += "<div id=\"myTabContent\" class=\"tab-content\">";
  text += "<div role=\"tabpanel\" class=\"tab-pane fade in active\" id=\"time\" aria-labelledBy=\"time-tab\">";
  text += "<table class=\"table table-hover\">";
  text += "<tr class=\"active\">";
  text += "<td><b>Start</b></td>";
  text += "<td><b>End</b></td>";
  text += "<td><b>Delta</b></td>";
  text += "<td><b>Interrupt</b></td></tr>";
  text += "<tr><td>"+stime+"</td>";
  text += "<td>"+etime+"</td>";
  text += "<td>"+delta+"</td>";
  text += "<td>"+inter+"</td>";
  text += "</tr></table></div>";
  // size
  text += "<div role=\"tabpanel\" class=\"tab-pane fade\" id=\"size\" aria-labelledBy=\"size-tab\">";
  text += "<table class=\"table table-bordered\">";
  text += "<tbody><tr>";
  text += "<th style=\"width: 10px\">#</th>";
  text += "<th>Type</th>";
  text += "<th>Progress</th>";
  text += "<th style=\"width: 40px\">Amount</th></tr>";
  text += "<tr><td>1.</td>";
    text += "<td>Estimated Size</td>";
    text += "<td><div class=\"progress progress-xs\">";
    text += "<div class=\"progress-bar progress-bar-yellow\" style=\"width:"+esize+"px\"></div></div></td>";
    text += "<td><span class=\"badge bg-aqua\">"+esize+"</span></td></tr></tr>";
  text += "<tr><td>2.</td>";
    text += "<td>Actual Size</td>";
    text += "<td><div class=\"progress progress-xs\">";
    text += "<div class=\"progress-bar progress-bar-success\" style=\"width:"+asize+"px\"></div></div></td>";
    text += "<td><span class=\"badge bg-aqua\">"+asize+"</span></td></tr></tr>";
  text += "<tr><td>3.</td>";
    text += "<td>Estimated Effort</td>";
    text += "<td><div class=\"progress progress-xs\">";
    text += "<div class=\"progress-bar progress-bar-yellow\" style=\"width:"+eeffort+"px\"></div></div></td>";
    text += "<td><span class=\"badge bg-aqua\">"+eeffort+"</span></td></tr></tr>";
  text += "<tr><td>4.</td>";
    text += "<td>Actual Effort</td>";
    text += "<td><div class=\"progress progress-xs\">";
    text += "<div class=\"progress-bar progress-bar-success\" style=\"width:"+aeffort+"px\"></div></div></td>";
    text += "<td><span class=\"badge bg-aqua\">"+aeffort+"</span></td></tr></tr>";
  text += "<tr><td>5.</td>";
  text += "<td>SLOC per per-mon</td>";
  text += "<td><div class=\"progress progress-xs\">";
  text += "<div class=\"progress-bar progress-bar-success\" style=\"width:"+per+"px\"></div></div></td>";
  text += "<td><span class=\"badge bg-aqua\">"+per+"</span></td></tr></tr>";
  text += "</tbody></table></div>";             
  // defect
  text += "<div role=\"tabpanel\" class=\"tab-pane fade\" id=\"defect\" aria-labelledBy=\"defect-tab\">";
  text += "<p>Not implemented yet. Sorry! ^_^b</p>";
  text += "</div></div></div></div></div> <!--panel-->";
  text += "</div></div></div></div></div></div>";
  
  var id = "spec" + name;
  var node = document.getElementById(id);
  node.innerHTML=text;
}

function newProjectLink(developerList){
  var list = developerList;
  var text = "";
  text += "<label>Project Name</label>";
  text += "<input class='form-control' name='name' placeholder='Enter name...'></input>";
  // choose developer
  text += "<label>Developers</label>";
  text += "<div class='dropdown'>";
  text += "<button class='btn btn-default dropdown-toggle' type='button' id='dropdownMenu1' data-toggle='dropdown' aria-haspopup='true' aria-expanded='true'>Dropdown<span class='caret'></span></button>";
  text += "<ul class='dropdown-menu' aria-labelledby='dropdownMenu1'>";
  var i;
  for (i = 0; i < list.length; i++) { 
    text += "<div class='checkbox'><input type='checkbox'>" + list[i].name +"</div>";
  }
  text += "</ul></div>";
  // SLOC
  text += "<label>Estimated Size (SLOC)</label>";
  text += "<input class='form-control' name='eSLOC' placeholder='Enter ...'></input>";
  // Effort
  text += "<label>Estimated Effort (person-month)</label>";
  text += "<input class=\"form-control\" name='eEffort' placeholder=\"Enter ...\"></input>";
  // phase description
  text += "<label>Descrpition</label>";
  text += "<textarea class=\"form-control\" rows=\"3\" name='desc' placeholder=\"Enter ...\"></textarea>";
  //text += "<input type=\"submit\" value='Create Project' style'display:inline-block;background-color: #80e174;'/></div>";
  text += "</div>";

  // footer
  text += "<div class='modal-footer'>";
  text += "<button type='button' class='btn btn-default' data-dismiss='modal'><i class='fa fa-fw fa-close'></i> Cancel</button>"
  text += "<button type='submit' id='createSubmit' style='margin: 10px' class='btn btn-primary')><i class='fa fa-mouse-pointer'></i> Create Project</button>"
  text += "</div>";

  var node = document.getElementById('newProject');
  node.innerHTML=text;
}

// not in use: problem with csrf_token
function closePhaseButton(){
  var token = '{% csrf_token %}';
  var text = "";
  text += "<div class='modal fade' id='endPhaseModal' tabindex='-1' role='dialog' aria-labelledby='endPhaseModalLabel'>";
  text += "<div class='modal-dialog' role='document'>";
  text += "<div class='modal-content' style='background: #e6e6e6'>";
  text += "<div class='modal-header'>";
  text += "<button type='button' class='close' data-dismiss='modal' aria-label='Close'><span aria-hidden='true'>&times;</span></button>";
  text += "<h3 class='modal-title'> Close Phase</h3></div>";
  // modal body
  text += "<div class='modal-body'>";
  text += "<form action='http://localhost:8000/pdt/endPhase/' method='post' id='closePhaseForm'>"+token;
  text += "<input class='form-control' type='hidden' name='phaseID' value='{{phase.id}}' readonly/>";
  text += "<label>Actual Size (SLOC)</label>";
  text += "<input class='form-control' name='aSLOC' placeholder='Enter ...'></input>";
  text += "</form>";
  // modal footer
  text += "<div class='modal-footer'>";
  text += "<button type='button' style='margin: 10px' class='btn btn-default' data-dismiss='modal'><i class='fa fa-fw fa-close'></i> Cancel</button>";
  text += "<button type='submit' id='endSubmit' style='margin: 10px' class='btn btn-primary')><i class='fa fa-mouse-pointer'></i> Close Phase</button>";
  text += "</div></div></div></div></div>";

  var node = document.getElementById('closePhaseModal');
  node.innerHTML=text;
}

function delcfm() { 
    if (!confirm("Confirm to Logout?")){ 
        window.event.returnValue = false; 
    } 
}

$("#AssignButton").click(function(){
      $("#Unassigned option:selected").each(function(){
        $("#Assigned").append($(this));
      });
});
$("#RemoveButton").click(function(){
  $("#Assigned option:selected").each(function(){
    $("#Unassigned").append($(this));
  });
});

$("#createSubmit").click(function() {
    var selectBox = document.getElementById("Assigned");

    for (var i = 0; i < selectBox.options.length; i++) 
    { 
         selectBox.options[i].selected = true; 
    }
    $('#newProjectForm').submit();
});