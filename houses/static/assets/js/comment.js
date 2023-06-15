    function toggleCommentInput(event, blogId) {
        event.preventDefault();

        // Close any previously open comment sections
        var commentSections = document.querySelectorAll('.mb-3');
        commentSections.forEach(function(section) {
            section.style.display = 'none';
        });

        // Open the clicked comment section
        var commentInput = document.querySelector('#comment-input-' + blogId);
        commentInput.style.display = 'block';
    }


    function submitComment(event, blogId) {
        event.preventDefault();
        const form = document.getElementById('comment-form-' + blogId);
        const formData = new FormData(form);

        fetch(form.action, {
            method: 'POST',
            body: formData,
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Comment submission successful, handle as needed (e.g., display success message)
                    console.log('Comment submitted successfully');
                } else {
                    // Comment submission failed, handle as needed (e.g., display error message)
                    console.error('Comment submission failed');
                }
            })
            .catch(error => {
                // Handle fetch error, if any
                console.error('An error occurred during comment submission:', error);
            });
    }
