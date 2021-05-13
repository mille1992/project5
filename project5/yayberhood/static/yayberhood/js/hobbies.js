document.addEventListener('DOMContentLoaded',function(){
    document.querySelectorAll('[name="expandPost"]').forEach(post => {
        post.clickedBool = false;
        post.addEventListener('click', event => {
            clickedPost = event.target;
            clickedPostProjectId = clickedPost.dataset.projectid;
            if (post.clickedBool == false){
                document.querySelector(`#expandedPostView_${clickedPostId}`).style.display = "block";
                post.clickedBool = true;
            }else{
                document.querySelector(`#expandedPostView_${clickedPostId}`).style.display = "none";
                post.clickedBool = false;
            }
        });
    });
});