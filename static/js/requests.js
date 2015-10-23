function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function get_new_request_count (){
        $.ajax({
            url: "/requests_api/",
            type: "GET",
            success: function(json) {
                new_requests_cnt = json['new_requests_cnt'];
                if (new_requests_cnt > 1){
                  update_request_page();
                }
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
}

function update_request_page (){
    $('form').empty();
    $('form').load(document.URL+ ' form');
    $('title').load(document.URL+ ' title');
}

$(document).ready(function(){
    $(document).on('click', '.priority', function() {
        var request_id ='';
        var priority_str= '';
        request_id += $(this).attr("id");
        priority_str += $("#input-"+request_id).val();
        update_request_page();
        $.ajax({
            dataType: "json",
            url: '/requests/',
            method: 'POST',
            data: {'request_id': request_id,
                'priority': priority_str},
            success: function() {
            }
        });
    });
    setInterval(get_new_request_count,1000);
});