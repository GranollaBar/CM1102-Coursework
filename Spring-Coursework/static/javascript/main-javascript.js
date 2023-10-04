const search = () => {
    const searchbox = document.getElementById("search-item").value.toUpperCase();
    const storeitems = document.getElementById("mainContentBox")
    const product = document.querySelectorAll(".finalProduct")
    const pname = storeitems.getElementsByTagName("h6")

    for (var i=0; i < pname.length; i++){
        let match = product[i].getElementsByTagName('h6')[0];
        if (match){
            let textvalue = match.textContent || match.innerHTML
            if (textvalue.toUpperCase().indexOf(searchbox) > -1){
                product[i].style.display = "";
            } else{
                product[i].style.display = "none";
            }
        }
    }
}

function ConfirmLogout(){
    var elems = document.getElementById('logoutButton');
    var confirmit = function (e) {
        if (!confirm('Are you sure you want to log out?')) e.preventDefault();
    };
    for (var i=0, l = elems.length; i < l; i++){
        elems[i].addEventListener('click', confirmit, false);
    }
}


function TypeSort(){
    document.getElementById('sixthProduct').style.top = '110px';
    document.getElementById('ninethProduct').style.top = '550px';
    document.getElementById('seventhProduct').style.top = '990px';
    document.getElementById('eighthProduct').style.top = '1430px';
    document.getElementById('firstProduct').style.top = '1870px';
    document.getElementById('secondProduct').style.top = '2310px';
    document.getElementById('thirdProduct').style.top = '2750px';
    document.getElementById('fourthProduct').style.top = '3180px';
    document.getElementById('fifthProduct').style.top = '3600px';
}

function LToHSort(){
    document.getElementById('eighthProduct').style.top = '110px';
    document.getElementById('firstProduct').style.top = '550px';
    document.getElementById('thirdProduct').style.top = '990px';
    document.getElementById('seventhProduct').style.top = '1430px';
    document.getElementById('secondProduct').style.top = '1870px';
    document.getElementById('fourthProduct').style.top = '2310px';
    document.getElementById('sixthProduct').style.top = '2750px';
    document.getElementById('ninethProduct').style.top = '3180px';
    document.getElementById('fifthProduct').style.top = '3600px';
}

function OriginalSort(){
    document.getElementById('firstProduct').style.top = '110px';
    document.getElementById('secondProduct').style.top = '550px';
    document.getElementById('thirdProduct').style.top = '990px';
    document.getElementById('fourthProduct').style.top = '1430px';
    document.getElementById('fifthProduct').style.top = '1870px';
    document.getElementById('sixthProduct').style.top = '2310px';
    document.getElementById('seventhProduct').style.top = '2750px';
    document.getElementById('eighthProduct').style.top = '3180px';
    document.getElementById('ninethProduct').style.top = '3600px';

}

function HToLSort(){
    document.getElementById('fifthProduct').style.top = '110px';
    document.getElementById('ninethProduct').style.top = '550px'; 
    document.getElementById('sixthProduct').style.top = '990px';
    document.getElementById('fourthProduct').style.top = '1430px';
    document.getElementById('secondProduct').style.top = '1870px';
    document.getElementById('seventhProduct').style.top = '2310px';
    document.getElementById('thirdProduct').style.top = '2750px';
    document.getElementById('firstProduct').style.top = '3180px';
    document.getElementById('eighthProduct').style.top = '3600px';
}

function EnvironmentSort(){
    document.getElementById('seventhProduct').style.top = '110px';
    document.getElementById('eighthProduct').style.top = '550px';
    document.getElementById('firstProduct').style.top = '990px';
    document.getElementById('thirdProduct').style.top = '1430px';
    document.getElementById('ninethProduct').style.top = '1870px';
    document.getElementById('sixthProduct').style.top = '2310px';
    document.getElementById('secondProduct').style.top = '2750px';
    document.getElementById('fourthProduct').style.top = '3180px'; 
    document.getElementById('fifthProduct').style.top = '3600px';
}