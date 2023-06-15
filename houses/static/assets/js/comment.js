    function toggleCommentInput(event, blogId) {
        event.preventDefault();

        // Check if the clicked comment section is already open
        var commentInput = document.querySelector('#comment-input-' + blogId);
        var isOpen = commentInput.style.display === 'block';

        // Close any previously open comment sections
        var commentSections = document.querySelectorAll('.mb-3');
        commentSections.forEach(function(section) {
            section.style.display = 'none';
        });

        // Open or close the clicked comment section
        commentInput.style.display = isOpen ? 'none' : 'block';

        // Clear input fields if opening the comment section
        if (!isOpen) {
            var usernameInput = commentInput.querySelector('input[name="username"]');
            var commentTextInput = commentInput.querySelector('textarea[name="comment"]');
            usernameInput.value = '';
            commentTextInput.value = '';
        }

        // Clear input fields
        var usernameInput = commentInput.querySelector('input[name="username"]');
        var commentTextInput = commentInput.querySelector('textarea[name="comment"]');
        usernameInput.value = '';
        commentTextInput.value = '';
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
