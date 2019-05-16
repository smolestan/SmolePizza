function chkcontrol(j, t) {
    document.getElementById("addToCart").disabled = true;
    var total = 0;
    for (var i = 0; i < document.cartform.toppings.length; i++) {
        if (document.cartform.toppings[i].checked) {
            total = total + 1;
            if (total == t) {
                document.getElementById("addToCart").disabled = false;
            } else {
                document.getElementById("addToCart").disabled = true;
            }
        }
        if (total > t) {
            // alert("Please Select only " + t + " toppings")
            document.cartform.toppings[j].checked = false;
            document.getElementById("addToCart").disabled = false;
            return false;
        }
    }
}