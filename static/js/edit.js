$(document).ready(function () {

    var options = {

        beforeSend: function(form, options) {
            setTimeout(function() {
                    $("#success").hide();
                    $("#warning").hide();
                    $("#fail").hide();
                    $("#in_progress").fadeIn(300);
                    //$('input').fadeOut(1000);

                    $('fieldset').attr("disabled","enabled");

         },
                300)
        },

        success: function(responseText) {
            setTimeout(function() {
                    $('fieldset').removeAttr("disabled");
                    if (responseText == 'OK'){
                        $("#in_progress").hide();
                        $("#fail").hide();
                        $("#success").fadeIn(1000);
                        //$('input').fadeIn(1000);
                    } else {
                        $("#success").hide();
                        $('#in_progress').hide();
                        $("#fail").fadeIn(1000);

                        alert(responseText);
                    }
                },
                1000)
        },

         error:  function(xhr, str){
             $("#success").hide();
             $('#in_progress').hide();
             $("#fail").fadeIn(1000);
             $('fieldset').removeAttr("disabled");
            }
        };
    
    jQuery('#edit-form').ajaxForm(options);



$(function() {
    $("#edit-form").submit(upload);
});
    $("#fileUpload").on('change', function () {

        if (typeof (FileReader) != "undefined") {
            var image_holder = $("#image-holder");
            image_holder.empty();
            var reader = new FileReader();
            reader.onload = function (e) {
                $("<img />", {
                    "src": e.target.result,
                    "height":"200",
                    "width":"200",
                    "class": "thumb-image"
                }).appendTo(image_holder);

            }
            image_holder.show();
            reader.readAsDataURL($(this)[0].files[0]);
        } else {
            alert("This browser does not support FileReader.");
        }
    });
});

