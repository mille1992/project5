document.addEventListener('DOMContentLoaded',function(){
    document.querySelectorAll('[name="expandPost"]').forEach(post => {
        post.expandPostClicked_bool = false;
        post.addEventListener('click', event => {
            clickedPost = event.target;
            clickedPostId = clickedPost.dataset.postid;
            if (post.expandPostClicked_bool == false){
                clickedPost_expandedPostView = document.querySelector(`#expandedPostView_${clickedPostId}`)
                
                if(document.querySelector('.pageTitle').innerHTML == "Hobbies"){
                    clickedPost_expandedPostView.children[3].style.display = "block"
                }
                
                clickedPost_expandedPostView.classList.add("expandDetailedView")
                clickedPost_expandedPostView.classList.remove("shrinkDetailedView")
                post.expandPostClicked_bool = true;

            }else{
                clickedPost_expandedPostView = document.querySelector(`#expandedPostView_${clickedPostId}`)
                clickedPost_expandedPostView.classList.add("shrinkDetailedView")
                clickedPost_expandedPostView.classList.remove("expandDetailedView")
                post.expandPostClicked_bool = false;

                if(document.querySelector('.pageTitle').innerHTML == "Hobbies"){
                    clickedPost_expandedPostView.ontransitionend = () => {
                        if (post.expandPostClicked_bool == false){
                            clickedPost_expandedPostView.children[3].style.display = "none"
                        }
                    }
                }
            }
        });


    });
});