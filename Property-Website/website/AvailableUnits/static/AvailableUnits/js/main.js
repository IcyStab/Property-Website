
let showData = false

function toggleContent(id){
    let addressName = `listingContent${id}`
    let listingContent = document.getElementById(addressName)
    if (showData){
        showData = false
        listingContent.style.display = 'none'
    }
    else{
        showData = true
        listingContent.style.display = 'block'
        
    }
}
