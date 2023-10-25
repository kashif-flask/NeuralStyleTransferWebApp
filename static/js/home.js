function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onloadstart = function () {
            // Show loading indicator when the reading starts
            $('#loading-indicator').show();
        };
        reader.onload = function (e) {
            $('#imageResult')
                .attr('src', e.target.result);
            // Hide loading indicator when the image is loaded
            $('#loading-indicator').hide();
        };
        reader.readAsDataURL(input.files[0]);
    }
}

$(function () {
    $('#upload').on('change', function () {
        readURL(this);
    });
});

/*  ==========================================
    SHOW UPLOADED IMAGE NAME
* ========================================== */
var input = document.getElementById( 'upload' );


input.addEventListener( 'change', showFileName );
function showFileName( event ) {
  var input = event.srcElement;
  var fileName = input.files[0].name;
  var infoArea = document.getElementById( 'upload-label' );
  infoArea.textContent = 'File name: ' + fileName;
}