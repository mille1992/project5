document.addEventListener('DOMContentLoaded',function(){
    document.querySelectorAll('[name="expandPost"]').forEach(post => {
        post.clickedBool = false;
        post.addEventListener('click', event => {
            clickedPost = event.target;
            clickedPostProjectId = clickedPost.dataset.projectid;
            if (post.clickedBool == false){
                //document.querySelector(`#littleProjects-expandedPostView_${clickedPostProjectId}`).style.maxHeight = "999px";
                //document.querySelector(`#littleProjects-expandedPostView_${clickedPostProjectId}`).style.opacity = "1";
                //document.querySelector(`#littleProjects-expandedPostView_${clickedPostProjectId}`).style.display = "block";
                document.querySelector(`#littleProjects-expandedPostView_${clickedPostProjectId}`).classList.add("expandDetailedView")
                document.querySelector(`#littleProjects-expandedPostView_${clickedPostProjectId}`).classList.remove("shrinkDetailedView")
                post.clickedBool = true;
            }else{
                //document.querySelector(`#littleProjects-expandedPostView_${clickedPostProjectId}`).style.maxHeight = "0px";
                //document.querySelector(`#littleProjects-expandedPostView_${clickedPostProjectId}`).style.opacity = "0";
                //document.querySelector(`#littleProjects-expandedPostView_${clickedPostProjectId}`).style.display = "none";
                document.querySelector(`#littleProjects-expandedPostView_${clickedPostProjectId}`).classList.add("shrinkDetailedView")
                document.querySelector(`#littleProjects-expandedPostView_${clickedPostProjectId}`).classList.remove("expandDetailedView")
                post.clickedBool = false;
            }
        });
    });
});