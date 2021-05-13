document.addEventListener('DOMContentLoaded',function(){
    document.querySelectorAll('[name="expandPost"]').forEach(post => {
        post.clickedBool = false;
        post.addEventListener('click', event => {
            clickedPost = event.target;
            clickedPostProjectId = clickedPost.dataset.projectid;
            if (post.clickedBool == false){
                document.querySelector(`#littleProjects-expandedPostView_${clickedPostProjectId}`).style.display = "block";
                post.clickedBool = true;
            }else{
                document.querySelector(`#littleProjects-expandedPostView_${clickedPostProjectId}`).style.display = "none";
                post.clickedBool = false;
            }
        });
    });
});