document.addEventListener('DOMContentLoaded',function(){
    document.querySelectorAll('[name="expandPost"]').forEach(post => {
        post.clickedBool = false;
        post.addEventListener('click', event => {
            clickedPost = event.target;
            clickedPostId = clickedPost.dataset.postId;
            console.log(clickedPost)
            console.log(clickedPostId)
            
            if (post.clickedBool == false){
                console.log(document.querySelector(`#expandedPostView_${clickedPostId}`))
                document.querySelector(`#expandedPostView_${clickedPostId}`).style.display = "block";
                post.clickedBool = true;
            }else{
                document.querySelector(`#expandedPostView_${clickedPostId}`).style.display = "none";
                post.clickedBool = false;
            }
        });
    });
});