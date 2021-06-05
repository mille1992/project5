document.addEventListener('DOMContentLoaded',function(){

    // show / hide category list to filter posts by category
    document.querySelectorAll('[name="hobbies-categoryName"]').forEach(categoryName => {
        categoryName.addEventListener('click', event => {
            // category list onclick: hide category list and save clicked value 
            clickedCategory = event.target;
            clickedCategoryName = clickedCategory.dataset.categoryname;
            document.getElementById('hobbies-category-list').style.display = "none";

            // Onclick: Toggle the category filter when clicking on the category button and hide posts
            categoryToggleButton = document.getElementById('hobbies-categoriesFilterToggle');
            categoryToggleButton.style.display = "block";
            categoryToggleButton.addEventListener('click', () => {
                document.getElementById('hobbies-category-list').style.display = "block";
                document.getElementById('hobbies-scrollView').style.display = "none";
            })


            document.getElementById('hobbies-scrollView').style.display = "block";
            document.querySelectorAll('[name="hobbies-outer-box"]').forEach(hobbyGroup => {
               categoryName = hobbyGroup.dataset.categoryname;
               if(clickedCategoryName == "All"){
                    hobbyGroup.style.display = "block";
               }
               else if (categoryName == clickedCategoryName){
                    hobbyGroup.style.display = "block";
               }
               else{
                    hobbyGroup.style.display = "none";
               }
            });
        });
    });


    
});