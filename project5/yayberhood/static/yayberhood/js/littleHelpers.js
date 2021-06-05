document.addEventListener('DOMContentLoaded',function(){
    document.cookie = "littleHelpers_helpType_onDisplay = None"
    document.querySelector('.littleHelpers-searches').classList.add("littleHelpers-typeDisabled")
    document.querySelector('.littleHelpers-offers').classList.add("littleHelpers-typeDisabled")

    document.querySelector('.littleHelpers-searches').addEventListener('click',event =>{
        clickedType = event.target.dataset.helptypevalue; 
        currHelpTypeOnDisplay = getCookie("littleHelpers_helpType_onDisplay")

        console.log(clickedType)
        console.log(currHelpTypeOnDisplay)

        if (clickedType != currHelpTypeOnDisplay){
            document.cookie = "littleHelpers_helpType_onDisplay = Searches"
    
            // style clicked button as enabled
            event.target.classList.add("littleHelpers-typeEnabled")
            event.target.classList.remove("littleHelpers-typeDisabled")

            // style not clicked button as disabled
            document.querySelector('.littleHelpers-offers').classList.remove("littleHelpers-typeEnabled")
            document.querySelector('.littleHelpers-offers').classList.add("littleHelpers-typeDisabled")
            

            document.querySelectorAll('.littleHelpers-outer-box').forEach(littleHelpersPost => {
                helpType = littleHelpersPost.dataset.helptype;
                if (helpType == clickedType){
                    littleHelpersPost.style.display = "block";
                }
                else{
                    littleHelpersPost.style.display = "none";
                }
             });
        }else{
            document.querySelectorAll('.littleHelpers-outer-box').forEach(littleHelpersPost => {
                littleHelpersPost.style.display = "block";
                document.cookie = "littleHelpers_helpType_onDisplay = None"

                // style button as disabled
                event.target.classList.remove("littleHelpers-typeEnabled")
                event.target.classList.add("littleHelpers-typeDisabled")
            });
        }
 
    })
    document.querySelector('.littleHelpers-offers').addEventListener('click',event=>{
        clickedType = event.target.dataset.helptypevalue;
        currHelpTypeOnDisplay = getCookie("littleHelpers_helpType_onDisplay")


        if (clickedType != currHelpTypeOnDisplay){
            document.cookie = "littleHelpers_helpType_onDisplay = Offers"

            // style button as enabled
            event.target.classList.add("littleHelpers-typeEnabled")
            event.target.classList.remove("littleHelpers-typeDisabled")

            // style not clicked button as disabled
            document.querySelector('.littleHelpers-searches').classList.remove("littleHelpers-typeEnabled")
            document.querySelector('.littleHelpers-searches').classList.add("littleHelpers-typeDisabled")

            document.querySelectorAll('.littleHelpers-outer-box').forEach(littleHelpersPost => {
                helpType = littleHelpersPost.dataset.helptype;

                if (helpType == clickedType){
                    littleHelpersPost.style.display = "block";
                }
                else{
                    littleHelpersPost.style.display = "none";
                }
             });
        }else{
            document.querySelectorAll('.littleHelpers-outer-box').forEach(littleHelpersPost => {
                littleHelpersPost.style.display = "block";
                document.cookie = "littleHelpers_helpType_onDisplay = None"

                // style button as disabled
                event.target.classList.remove("littleHelpers-typeEnabled")
                event.target.classList.add("littleHelpers-typeDisabled")
            });
        }
    })




    // show / hide category list to filter posts by category
    document.querySelectorAll('[name="littleHelpers-searchOfferSelect"]').forEach(categoryName => {
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