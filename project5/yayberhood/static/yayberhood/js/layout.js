document.addEventListener('DOMContentLoaded',function(){
    document.querySelectorAll('[name="expandPost"]').forEach(post => {
        post.expandPostClicked_bool = false;
        post.addEventListener('click', event => {
            clickedPost = event.target;
            clickedPostId = clickedPost.dataset.postid;
            if (post.expandPostClicked_bool == false){
                document.querySelector(`#expandedPostView_${clickedPostId}`).classList.add("expandDetailedView")
                document.querySelector(`#expandedPostView_${clickedPostId}`).classList.remove("shrinkDetailedView")
                post.expandPostClicked_bool = true;
            }else{
                document.querySelector(`#expandedPostView_${clickedPostId}`).classList.add("shrinkDetailedView")
                document.querySelector(`#expandedPostView_${clickedPostId}`).classList.remove("expandDetailedView")
                post.expandPostClicked_bool = false;
            }
        });

    });
});