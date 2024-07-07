// Wait for the DOM to be fully loaded
$(document).ready(function () {
    console.log('Document ready');

    // Select the schedule button element
    $('#schedule-btn').click(function () {
        // Get the datetime value from the datetimepicker input
        var datetime = $('#datetimepicker input').val();
        
        // Get the title value from the main-form input with name "title"
        var title = $('#main-form input[name="title"]').val();
        
        // Get the content value from the main-form textarea with name "content"
        var content = $('#main-form textarea[name="content"]').val();

        // Check if either the title or content is not empty
        if (title != '' || content != '') {
            // Send a POST request to the /new/scheduled/post endpoint
            $.ajax({
                // URL of the endpoint
                url: '/new/scheduled/post',
                // HTTP method to use
                method: 'POST',
                // Data to send with the request
                data: { datetime: datetime, title: title, content: content },
                // Function to call when the request is successful
                success: function (status) {
                    console.log('Success:', status);

                    // Check if the status is "True"
                    if (status == 'True') {
                        // Hide the modal
                        $('#myModal').modal('hide');
                        // Show an alert message
                        alert('Your post has been scheduled successfully!');
                        // Reload the page
                        location.reload();
                    } else {
                        // Show an alert message
                        alert('Scheduled date and time cannot be in the past');
                    }
                }
            });
        } else {
            // Show an alert message
            alert("Both Fields are required");  
        }
    });
});