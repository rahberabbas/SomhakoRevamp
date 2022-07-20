function windowScroll(){var t=document.getElementById("navbar");50<=document.body.scrollTop||50<=document.documentElement.scrollTop?t.classList.add("nav-sticky"):t.classList.remove("nav-sticky")}window.addEventListener("scroll",function(t){t.preventDefault(),windowScroll()});var tooltipTriggerList=[].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]')),tooltipList=tooltipTriggerList.map(function(t){return new bootstrap.Tooltip(t)});

// $("#profileid").val(data.id);
//                     $("#firstName").val(data.first_name);
//                     $("#lastName").val(data.last_name);
//                     $("#choices-single-categories").val(data.account_type);
//                     $("#exampleFormControlTextarea1").val(data.bio);
//                     $("#choices-single-location").val(data.location)
//                     $("#choices-single-experience").val(data.years_of_experience)
//                     console.log(data)