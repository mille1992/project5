document.addEventListener('DOMContentLoaded',function(){
    document.querySelectorAll('[name="hobbies-categoryName"]').forEach(categoryName => {
        categoryName.addEventListener('click', event => {
            clickedCategory = event.target;
            clickedCategoryName = clickedCategory.dataset.categoryname;
            document.getElementById('hobbies-category-list').style.display = "none";
            categoryToggleButton = document.getElementById('hobbies-categoriesFilterToggle');
            categoryToggleButton.style.display = "block";
            categoryToggleButton.addEventListener('click', () => {
                document.getElementById('hobbies-category-list').style.display = "block";
                document.getElementById('hobbies-scrollView').style.display = "none";
            })
            document.getElementById('hobbies-scrollView').style.display = "block";
            document.querySelectorAll('[name="hobbies-outer-box"]').forEach(hobbyGroup => {
               categoryName = hobbyGroup.dataset.categoryname;
               if (categoryName == clickedCategoryName){
                    hobbyGroup.style.display = "block";
               }
               else{
                    hobbyGroup.style.display = "none";
               }
            });
        });
    });
});