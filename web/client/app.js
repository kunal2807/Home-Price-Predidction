

var base_url = '/api'


function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");

    for(var i in uiBathrooms) {
        if(uiBathrooms[i].checked) {
            return parseInt(i)+1;
        }
    }
    return -1; // Invalid Value
}

function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for(var i in uiBHK) {
        if(uiBHK[i].checked) {
            return parseInt(i)+1;
        }
    }
    return -1; // Invalid Value
}

function getBalconyValue() {
    var uiBalcony = document.getElementsByName("uiBalcony");
    for(var i in uiBalcony) {
        if(uiBalcony[i].checked) {
            return parseInt(i)+1;
        }
    }
    return -1; // Invalid Value
}




function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft");
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var balcony = getBalconyValue();
    var location = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");

    var url = `${base_url}/predict-home-price`;

    $.post(url, {
        total_sqft: parseFloat(sqft.value),
        bhk: bhk,
        bath: bathrooms,
        location: location.value,
        balcony: balcony
    },function(data, status) {
        console.log(data);
        estPrice.innerHTML = "<h2>" + data.house_price.toString() + " Lakh</h2>";
        console.log(status);
    });
}


function onPageLoad(){
console.log('page loaded... ')
var url = `${base_url}/get-location-names`
$.get(url, (data, status)=>{
    if(!data) return
    let options = document.getElementById('uiLocations')
    for(let x in options) options.remove(x)
    data.locations.map( location => {
        var newOption = new Option(location)
        options.append(newOption)
    })
})
}




window.onload = onPageLoad