document.addEventListener('DOMContentLoaded',function(){
    document.cookie = "borrowIt_rentalType_onDisplay = None"
    document.querySelector('.borrowIt-searches').classList.add("borrowIt-typeDisabled")
    document.querySelector('.borrowIt-offers').classList.add("borrowIt-typeDisabled")

    document.querySelector('.borrowIt-searches').addEventListener('click',event =>{
        clickedType = event.target.dataset.rentaltypevalue; 
        currRentalTypeOnDisplay = getCookie("borrowIt_rentalType_onDisplay")

        if (clickedType != currRentalTypeOnDisplay){
            document.cookie = "borrowIt_rentalType_onDisplay = Searches"
    
            // style clicked button as enabled
            event.target.classList.add("borrowIt-typeEnabled")
            event.target.classList.remove("borrowIt-typeDisabled")

            // style not clicked button as disabled
            document.querySelector('.borrowIt-offers').classList.remove("borrowIt-typeEnabled")
            document.querySelector('.borrowIt-offers').classList.add("borrowIt-typeDisabled")
            

            document.querySelectorAll('.borrowIt-outer-box').forEach(borrowItPost => {
                rentalType = borrowItPost.dataset.rentaltype;
                if (rentalType == clickedType){
                    borrowItPost.style.display = "block";
                }
                else{
                    borrowItPost.style.display = "none";
                }
             });
        }else{
            document.querySelectorAll('.borrowIt-outer-box').forEach(borrowItPost => {
                borrowItPost.style.display = "block";
                document.cookie = "borrowIt_rentalType_onDisplay = None"

                // style button as disabled
                event.target.classList.remove("borrowIt-typeEnabled")
                event.target.classList.add("borrowIt-typeDisabled")
            });
        }
 
    })
    document.querySelector('.borrowIt-offers').addEventListener('click',event=>{
        clickedType = event.target.dataset.rentaltypevalue;
        currRentalTypeOnDisplay = getCookie("borrowIt_rentalType_onDisplay")

        if (clickedType != currRentalTypeOnDisplay){
            document.cookie = "borrowIt_rentalType_onDisplay = Offers"

            // style button as enabled
            event.target.classList.add("borrowIt-typeEnabled")
            event.target.classList.remove("borrowIt-typeDisabled")

            // style not clicked button as disabled
            document.querySelector('.borrowIt-searches').classList.remove("borrowIt-typeEnabled")
            document.querySelector('.borrowIt-searches').classList.add("borrowIt-typeDisabled")

            document.querySelectorAll('.borrowIt-outer-box').forEach(borrowItPost => {
                rentalType = borrowItPost.dataset.rentaltype;
                if (rentalType == clickedType){
                    borrowItPost.style.display = "block";
                }
                else{
                    borrowItPost.style.display = "none";
                }
             });
        }else{
            document.querySelectorAll('.borrowIt-outer-box').forEach(borrowItPost => {
                borrowItPost.style.display = "block";
                document.cookie = "borrowIt_rentalType_onDisplay = None"

                // style button as disabled
                event.target.classList.remove("borrowIt-typeEnabled")
                event.target.classList.add("borrowIt-typeDisabled")
            });
        }
    })




    // show / hide category list to filter posts by category
    document.querySelectorAll('[name="borrowIt-searchOfferSelect"]').forEach(categoryName => {
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

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
      var c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }