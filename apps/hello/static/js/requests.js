/**
 * Created by torhammer on 11.09.15.
 */

function add_req (){
        var url = "/requests_api/"; //init url

        $.ajax({
            url: url,
            type: "GET",
            success: function(json) {
                new_requests_cnt = json['new_requests_cnt'];
                console.log("JS new_requests_cnt = " + new_requests_cnt);

                if (new_requests_cnt > 0){
                    document.title = '(' + new_requests_cnt +') New requests';
                }else{
                    document.title = 'No new requests';
                }

                requests_array = json['last_10_requests'];
                console.log("last_10_requests = " + requests_array.toString);
                for(var i=requests_array.length-1; i >= 0; i--){
                    var request_record = $('<tr class ="request_unreaded"></tr>');
                    request_record.append( '<td>' + requests_array[i]['id'] +'</td>');
                    request_record.append( '<td>' + requests_array[i]['method'] +'</td>');
                    request_record.append( '<td>' + requests_array[i]['uri'] +'</td>');
                    request_record.append( '<td>' + requests_array[i]['status_code'] +'</td>');
                    request_record.append( '<td>' + requests_array[i]['remote_addr'] +'</td>');
                    $('#webrequest_block').prepend(request_record);

                    if ($('tbody tr').length > 10){
                        $('tbody tr:last').remove();
                    }
                }
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }

$(document).ready(function(){
    add_req();

  $('.table').click(function () {
      add_req();
  });

    setInterval('add_req()',1000);
});