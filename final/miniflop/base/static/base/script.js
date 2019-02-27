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
var day_start = 8*60 ;
var day_end = 18*60 + 45 ;


// data
var tutors = [] ;
var modules = [] ;
var rooms = [] ;
var courses = [] ;

// display
var margin = {top: 10, bot:10, left:10, right:10};
var min_to_px = 1 ;
var gp = {width: 30, nb_max: 7} ;
var tutor_filter = {nb_col: 10, width: 30, height: 30, h_margin: 2, v_margin: 2, bg: "#000080"};


function init() {
    
    d3.select("svg")
        .attr("height", svg_height())
        .attr("width", svg_width()) ;

    for(var i = 0 ; i<days.length ; i++){
        idays[days[i].ref] = days[i].num ;
    }

    groups["CE"] = {start: 0, width: 7} ;
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
        url: url_data,
        async: true,
        contentType: "text/csv",
        success: function(msg, ts, req) {
            tutors = [];
            modules = [];
            rooms = [];
            
            courses = d3.csvParse(msg, translate_courses_from_csv);

            display_courses() ;
            display_grid() ;
//            display_tutor_filters() ;            
        },
        error: function(msg) {
            console.log("error");
        }
    });

}


function translate_courses_from_csv(d) {
    var ind = tutors.indexOf(d.prof_nom);
    if (ind == -1) {
        tutors.push(d.prof_nom);
    }
    if (modules.indexOf(d.module) == -1) {
        modules.push(d.module);
    }
    if (rooms.indexOf(d.room) == -1) {
        rooms.push(d.room);
    }
    var co = {
        id_cours: +d.id_course,
        tutor: d.tutor_name,
        group: d.gp_name,
        module: d.module,
	c_type: d.coursetype,
        day_ref: d.day,
        start: +d.start_time,
        duration: +d.duration,
        room: d.room,
	room_type: d.room_type,
	color_bg: d.color_bg,
	color_txt: d.color_txt,
    };
    return co;
}




/*---------------------
  -- DISPLAY COURSES --
  ---------------------*/


function display_courses() {
    var c_layer = d3.select(".courses-layer");

    var c_all = c_layer
        .selectAll(".course")
        .data(courses) ;

    var c_groups = c_all
        .enter()
        .append("g")
        .attr("class", "course") ;

    c_groups
        .append("rect")
        .attr("x", course_x)
        .attr("y", course_y)
        .attr("width", course_width)
        .attr("height", course_height)
        .attr("fill", course_fill);

    c_groups
        .append("text")
        .text(course_module_txt)
        .attr("x",course_mid_x)
        .attr("y",course_module_y)
        .attr("fill", course_txt_fill);
    c_groups
        .append("text")
        .text(course_tutor_txt)
        .attr("x",course_mid_x)
        .attr("y",course_tutor_y)
        .attr("fill", course_txt_fill);
    c_groups
        .append("text")
        .text(course_room_txt)
        .attr("x",course_mid_x)
        .attr("y",course_room_y)
        .attr("fill", course_txt_fill);
    
}

function display_grid() {
    var c_layer = d3.select(".grid-layer");

    var c_all = c_layer
        .selectAll(".day")
        .data(days) ;

    c_all
        .enter()
        .append("rect")
        .attr("class", "day")
        .attr("x", day_x)
        .attr("y", day_y)
        .attr("width", day_width)
        .attr("height", day_height)
        .attr("stroke-width", 5)
        .attr("stroke", "black")
        .attr("fill", "none");
}

/*---------------------
  -- DISPLAY HELPERS --
  ---------------------*/
function course_x(c) {
    return idays[c.day_ref] * gp.nb_max * gp.width
        + groups[c.group].start * gp.width  ;
}
function course_width(c) {
    return groups[c.group].width * gp.width ;
}
function course_y(c) {
    return (c.start - day_start) * min_to_px ;
}
function course_height(c) {
    return c.duration * min_to_px ;
}
function course_fill(c) {
    return c.color_bg ;
}

function course_txt_fill(c) {
    return c.color_txt ;
}

function course_module_txt(c) {
    return c.module ;
}
function course_tutor_txt(c) {
    return c.tutor ;
}
function course_room_txt(c) {
    return c.room ;
}
function course_mid_x(c) {
    return course_x(c) + course_width(c)/2 ;
}
function course_module_y(c) {
    return course_y(c) + course_height(c)/4 ;
}
function course_tutor_y(c) {
    return course_y(c) + 2*course_height(c)/4 ;
}
function course_room_y(c) {
    return course_y(c) + 3*course_height(c)/4 ;
}

function day_x(d) {
    return d.num * gp.nb_max * gp.width ;
}
function day_y() {
    return 0 ;
}
function day_width() {
    return gp.nb_max * gp.width ;
}
function day_height() {
    return (day_end - day_start) * min_to_px ;
}

function tutor_x(t, i) {
    return (i % tutor_filter.nb_col) * (tutor_filter.width + tutor_filter.h_margin) ;
}
function tutor_y(t, i) {
    return day_height() + 10 +
        Math.floor(i / tutor_filter.nb_col) * (tutor_filter.height + tutor_filter.v_margin) ;
}
function tutor_width() {
    return tutor_filter.width ;
}
function tutor_height() {
    return tutor_filter.height ;
}
function tutor_txt(t) {
    return t ;
}
function tutor_fill(t) {
    return tutor_filter.bg ;
}
function tutor_txt_x(t, i) {
    return tutor_x(t, i) + tutor_width()/2 ;
}
function tutor_txt_y(t, i) {
    return tutor_y(t, i) + tutor_height()/2 ;
}
function tutor_txt_fill() {
    return "white" ;
}


function svg_height() {
    return (day_end - day_start) * min_to_px + 200 ;
}
function svg_width() {
    return days.length * gp.nb_max * gp.width ;
}
/*------------------
  ------ RUN -------
  ------------------*/

init();
fetch_courses() ;
