// function reportButton(name, stime, etime, deltaH, deltaM, deltaS, inter, esize, asize, eeffort, aeffort, per){
function reportButton(name, stime, etime, delta, inter, esize, asize, eeffort, aeffort, per){
  var text = "";
  text += "<div class='modal fade' id='reportModal"+name+"' tabindex='-1' role='dialog' aria-labelledby='reportModalLabel'>";
  text += "<div class='modal-dialog' role='document'>";
  text += "<div class='modal-content'>";
  text += "<div class='modal-header'>";
  text += "<button type='button' class='close' data-dismiss='modal' aria-label='Close'><span aria-hidden='true'>&times;</span></button>";
  text += "<h4 class='modal-title'>Metrics</h4></div>";
  
  // modal body
  text += "<div class='modal-body'>";
  text += "<div class='row'><div class='col-md-12'>";
  text += "<div class='panel panel-default'><div class='panel-body'>";
  text += "<div class='bs-example bs-example-tabs' data-example-id='togglable-tabs'>";
  text += "<ul id='myTabs' class='nav nav-tabs' role='tab-list'>";
  text += "<li role='presentation' class='active'><a href='#time"+name+"' id='time-tab"+name+"' role='tab' data-toggle='tab' aria-controls='time"+name+"' aria-expanded='true'>Time</a></li>";

  text += "<li role='presentation'><a href='#size"+name+"' role='tab' id='size-tab"+name+"' data-toggle='tab' aria-controls='size"+name+"'>Size</a></li>";
  // time
  text += "<div id='myTabContent"+name+"' class='tab-content'>";
  text += "<div role='tabpanel' class='tab-pane fade in active' id='time"+name+"' aria-labelledBy='time-tab"+name+"'>";
  text += "<table class='table table-hover'>";
  text += "<tr class='active'>";
  text += "<td><b>Start</b></td>";
  text += "<td><b>End</b></td>";
  text += "<td><b>Delta</b></td>";
  text += "<td><b>Interrupt</b></td></tr>";
  text += "<tr><td>"+stime+"</td>";
  text += "<td>"+etime+"</td>";
  //text += "<td>"+deltaH+'h '+deltaM+'min '+deltaS+'s '+"</td>";
  text += "<td>"+delta+"</td>";
  text += "<td>"+inter+"</td>";
  text += "</tr></table></div>";
  // size
  text += "<div role='tabpanel' class='tab-pane fade' id='size"+name+"' aria-labelledBy='ize-tab"+name+"'>";
  text += "<table class='table table-bordered'>";
  text += "<tbody><tr>";
  text += "<th style='width: 10px'>#</th>";
  text += "<th>Type</th>";
  text += "<th>Progress</th>";
  text += "<th style='width: 40px'>Amount</th></tr>";
  text += "<tr><td>1.</td>";
    text += "<td>Estimated Size</td>";
    text += "<td><div class='progress progress-xs'>";
    var eKsize = esize / 1000;
    var eKsizeW = esize;
    while (eKsizeW > 200)
      eKsizeW = eKsizeW / 5;
    text += "<div class='progress-bar progress-bar-yellow' style='width:"+eKsizeW+"px'></div></div></td>";
    text += "<td><span class='badge bg-aqua'>"+eKsize+" k</span></td></tr></tr>";
  text += "<tr><td>2.</td>";
    text += "<td>Actual Size</td>";
    text += "<td><div class='progress progress-xs'>";
    var aKsize = asize / 1000;
    var aKsizeW = asize;
    while (aKsizeW > 200)
      aKsizeW = aKsizeW / 5;
    text += "<div class='progress-bar progress-bar-success' style='width:"+aKsizeW+"px'></div></div></td>";
    text += "<td><span class='badge bg-aqua'>"+aKsize+" k</span></td></tr></tr>";
  text += "<tr><td>3.</td>";
    text += "<td>Estimated Effort</td>";
    text += "<td><div class='progress progress-xs'>";
    text += "<div class='progress-bar progress-bar-yellow' style='width:"+eKsizeW+"px'></div></div></td>";
    text += "<td><span class='badge bg-aqua'>"+eeffort+"</span></td></tr></tr>";
  text += "<tr><td>4.</td>";
    text += "<td>Actual Effort</td>";
    text += "<td><div class='progress progress-xs'>";
    text += "<div class='progress-bar progress-bar-success' style='width:"+aKsizeW+"px'></div></div></td>";
    text += "<td><span class='badge bg-aqua'>"+aeffort+"</span></td></tr></tr>";
  text += "<tr><td>5.</td>";
  text += "<td>SLOC per per-mon</td>";
  text += "<td><div class='progress progress-xs'>";
  var perK = per;
  var perKWidth = per;
  while (perKWidth > 200)
    perKWidth = perKWidth / 5;
  text += "<div class='progress-bar progress-bar-success' style='width:"+perKWidth+"px'></div></div></td>";
  text += "<td><span class='badge bg-aqua'>"+perK+"</span></td></tr></tr>";
  text += "</tbody></table></div>";             
  text += "</div></div></div></div></div></div>";
  
  var id = "spec" + name;
  var node = document.getElementById(id);
  node.innerHTML=text;
}

function newPhaseButton(projID){
  var text = "";
  text += "<label>Phase</label>";
  text += "<select class='form-control' name='name'>";
  text += "<option>Inception</option>";
  text += "<option>Elaboration</option>";
  text += "<option>Construction</option>";
  text += "<option>Transition</option>";
  text += "</select>";
  // SLOC
  text += "<label>Estimated Size (SLOC)</label>";
  text += "<input class=\"form-control\" name='eSLOC' placeholder=\"Enter ...\"></input>";//</div>";
  // Effort
  text += "<label>Estimated Effort (person-month)</label>";
  text += "<input class=\"form-control\" name='eEffort' placeholder=\"Enter ...\"></input>";//</div>";
  // phase description
  text += "<label>Descrpition (optional)</label>";
  text += "<textarea class=\"form-control\" rows=\"3\" name='desc' placeholder=\"Enter ...\"></textarea>";//</div>";

  // footer
  text += "<div class='modal-footer'>";
  text += "<button type='button' class='btn btn-default' data-dismiss='modal'><i class='fa fa-fw fa-close'></i> Cancel</button>"
  text += "<button type='submit' id='createPhaseSubmit' style='margin: 10px' class='btn btn-primary')><i class='fa fa-mouse-pointer'></i> Create Phase</button>"
  text += "</div>";

  var node = document.getElementById('newPhase');
  node.innerHTML=text;
}

function newIterButton(){
  var text = "";
  // SLOC
  text += "<label>Estimated Size (SLOC)</label>";
  text += "<input class=\"form-control\" name='eSLOC' placeholder=\"Enter ...\"></input>";//</div>";
  // Effort
  text += "<label>Estimated Effort (person-month)</label>";
  text += "<input class=\"form-control\" name='eEffort' placeholder=\"Enter ...\"></input>";//</div>";
  // phase description
  text += "<label>Descrpition</label>";
  text += "<textarea class=\"form-control\" rows=\"3\" name='desc' placeholder=\"Enter ...\"></textarea>";//</div>";

  // footer
  text += "<div class='modal-footer'>";
  text += "<button type='button' class='btn btn-default' data-dismiss='modal'><i class='fa fa-fw fa-close'></i> Cancel</button>"
  text += "<button type='submit' id='createIterSubmit' style='margin: 10px' class='btn btn-primary')><i class='fa fa-mouse-pointer'></i> Open Iteration</button>"
  text += "</div>";

  var node = document.getElementById('newIteration');
  node.innerHTML=text;
}

// submit button for Close Project
$("#endProjectSubmit").click(function() {
  $('#closeProjectForm').submit();
});

// submit button for New Phase
$("#createPhaseSubmit").click(function() {
  $('#newPhaseForm').submit();
});
// submit button for Close Phase
$("#endPhaseSubmit").click(function() {
  $('#closePhaseForm').submit();
});

// submit button for New Iteration
$("#createIterSubmit").click(function() {
  $('#newIterForm').submit();
});
// submit button for Close Iteration
$("#endIterSubmit").click(function() {
  $('#closeIterForm').submit();
});

function delcfm() { 
    if (!confirm("Confirm to Logout?")){ 
        window.event.returnValue = false; 
    } 
}