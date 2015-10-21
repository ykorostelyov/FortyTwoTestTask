/**
 * Created by torhammer on 11.09.15.
 */
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

function update_request_page (){
    $('form').empty();
    $('form').load(document.URL+ ' form');
    $('title').load(document.URL+ ' title');
}

$(document).ready(function(){
    $(document).on('change', '.priority', function() {
        var priority_str ='';
        $(this.children).each(function() {
            if(this.selected) {
                priority_str += $(this).val() + " ";
            }
        });

        $.ajax({
            dataType: "json",
            url: '/requests/',
            method: 'POST',
            data: {'request_id': this.getAttribute('request-id'),
                'priority': priority_str},
            success: function() {
            }
        });
    });

    setInterval(update_request_page,6000);
});