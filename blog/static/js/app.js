function filter(){
	document.getElementById('filter').classList.toggle("activate");
}

function AddType(){
    document.getElementById('form-type').classList.toggle("active-form");
}

function ClickBurger(){
    document.getElementById('nav').classList.toggle("active-nav");
    if (document.getElementById('burger').className == "burger"){
        document.getElementById('burger').className = "burger-click";
        document.getElementById('admin').className = "box-admin-visible";
    }else{
        document.getElementById('burger').className = "burger";
        document.getElementById('admin').className = "box-admin";
    }
    
}