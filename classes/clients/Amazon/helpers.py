node_data_fn = ```
function getStoreText(){
  return document.querySelector('#bylineInfo').innerText;
}

function getDetails(){
  document.querySelector('.a-expander-prompt').click();
  const rows = document.querySelectorAll('#productOverview_feature_div .a-row:not(#poExpander)');
  const details = {}
  for (const row of rows){
    const [k, v] = row.innerText.split('\n');
    details[k] = v;
  }
  return details;
}

function getProductId(){
  const currentURL = window.location.href;
  const match = currentURL.match('\/[A-Z0-9]{10}')
  return match[0].slice(1)
}

function getNodeData(){
  const storeText = getStoreText()
  const details = getDetails()
  const productId = getProductId()
  return {
    storeText,
    details,
    productId,
  }
  
  
}
function formatData(data){
  const {storeText, details, productId} = data
  return `    "storeText": "${storeText}",
    "details": ${JSON.stringify(details, null, 2)},
    "productId": "${productId}",`
}
console.log(formatData(getNodeData()));
```