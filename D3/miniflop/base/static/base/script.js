/*------------------------
  ------ VARIABLES -------
  ------------------------*/

// input
var days = [{num: 0, ref: "m", name: "Lun."},
            {num: 1, ref: "tu", name: "Mar."},
            {num: 2, ref: "w", name: "Mer."},
            {num: 3, ref: "th", name: "Jeu."},
            {num: 4, ref: "f", name: "Ven."}] ;
var idays = {};
var groups = {} ;
var day_start =8*60 ;
var day_end = 18*60 + 45 ;


// data
var courses = [] ;

// display settings
var min_to_px = 1 ;
var gp = {width: 30, nb_max: 7} ;


// initialisation function
function init() {
    
    d3.select("svg")
        .attr("height", svg_height())
        .attr("width", svg_width()) ;

    for(var i = 0 ; i<days.length ; i++){
        idays[days[i].ref] = days[i].num ;
    }

    groups["CE"] = {start: 0, width: 6} ;
    groups["1"] =  {start: 0, width: 2} ;
    groups["1A"] = {start: 0, width: 1} ;
    groups["1B"] = {start: 1, width: 1} ;
    groups["2"] =  {start: 2, width: 2} ;
    groups["2A"] = {start: 2, width: 1} ;
    groups["2B"] = {start: 3, width: 1} ;
    groups["3"] =  {start: 4, width: 2} ;
    groups["3A"] = {start: 4, width: 1} ;
    groups["3B"] = {start: 5, width: 1} ;
    groups["4"] =  {start: 6, width: 1} ;
    groups["234"]= {start: 2, width: 5} ;
}



/*------------------------
  ---- READ DATA FILE ----
  ------------------------*/

function fetch_courses() {

    $.ajax({
        type: "GET",
        dataType: 'text',
        url: data,
        async: true,
        contentType: "text/csv",
        success: function(msg, ts, req) {
            courses=d3.csvParse(msg);
            for(var i=0;i<courses.length;i++){
                console.log(courses[i]);
            }
            dislay_grille();
            dislay_courses();
        },
        error: function(msg) {
            console.log("Error while reading the courses.");
        }
    });

}



function svg_height() {
    return (day_end - day_start) * min_to_px + 200 ;
}
function svg_width() {
    return days.length * gp.nb_max * gp.width ;
}

function day_width() {
    return gp.nb_max * gp.width;
}

function day_height() {
    return (day_end-day_start)*min_to_px;
}

function day_x(day) {
    return day.num*day_width();
}

function day_y(day) {
    return 0;
}


function course_width(c) {
    return groups[c.gp_name].width*gp.width;
}

function course_color(c) {
    return c.color_bg;
}

function course_height(c) {
    return c.duration*min_to_px;
}

function course_x(c) {
    return day_x(days[idays[c.day]])+groups[c.gp_name].start*gp.width;
}

function course_y(c) {
    return c.start_time-day_start;
}

function course_module(c) {
    var chaine=c.module;
    return chaine;
}

function course_textx(c) {
    return (groups[c.gp_name].width*gp.width)/2+day_x(days[idays[c.day]])+groups[c.gp_name].start*gp.width;
}

function course_texty(c) {
    return c.start_time-day_start+(c.duration*min_to_px)/2;
}


function dislay_courses() {
    var grid=d3.select(".courses-layer");
    grid.selectAll("rect")
        .data(courses)
        .enter()
        .append("rect")
        .attr("x",course_x)
        .attr("y",course_y)
        .attr("width",course_width)
        .attr("height",course_height)
        .attr("stroke","black")
        .attr("fill",course_color);
        
        grid.selectAll("text")
        .data(courses)
        .enter()
        .append("text")
        .text(course_module)
        .attr("stroke","black")
        .attr("x",course_textx)
        .attr("y",course_texty)
        .attr("font-size",8);
}

function dislay_grille() {
    var grid=d3.select(".grid-layer");
    grid.selectAll("rect")
        .data(days)
        .enter()
        .append("rect")
        .attr("x",day_x)
        .attr("y",day_y)
        .attr("width",day_width())
        .attr("height",day_height())
        .attr("stroke","black")
        .attr("fill","transparent");
}

/*------------------
  ------ RUN -------
  ------------------*/

init();
fetch_courses() ;
