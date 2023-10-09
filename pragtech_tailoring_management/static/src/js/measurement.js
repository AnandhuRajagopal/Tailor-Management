function openMeasurementPopup(clothTypeId) {
    $('#measurement_popup').modal('show'); // Show the modal
}
function closeMeasurementPopup() {
    $('#measurement_popup').modal('hide');
}


function submit_measurement() {
    var product_id = $('#product_id').val();

    // Send the product ID to the server to fetch the measurements
    $.ajax({
        url: '/website_measurement/submit',
        type: 'POST',
        data: {
            cloth_type_id: product_id
        },
        success: function (response) {
            if (response.success) {
                // Update the measurement modal with the measurements from the server
                $('#measurement_popup .modal-body').html('');
                for (var i in response.measurements) {
                    var measurement = response.measurements[i];
                    var input = $('<input type="text" class="form-control" id="measurement_' + measurement.name + '" name="measurement_' + measurement.name + '" required="1" />');
                    input.val(measurement.value);
                    $('#measurement_popup .modal-body').append(input);
                }

                // Show the measurement modal
                $('#measurement_popup').modal('show');
            } else {
                // Show an error message
                alert(response.message);
            }
        }
    });
}
