function getTitle(node){
	return node.querySelectorAll('h2 span')[0].innerText
}
function getRating(node){
  const ratingNode = node.querySelector('.a-icon.a-icon-star-small.aok-align-bottom span');
  const countNode = node.querySelector('.a-size-mini.a-color-base.s-light-weight-text');
  if (!ratingNode || !countNode) return null;
	const ratingText = ratingNode.innerText
	const countText = countNode.innerText
	
	return {
		rating: parseInt(ratingText.split(" ")[0]),
		count: parseInt(countText)
	}
}
function getPrice(node){
  const wholeNode = node.querySelector('.a-price .a-price-whole');
  if (!wholeNode) return null;

	const wholeText = node.querySelector('.a-price .a-price-whole').innerText.replace('.','').replace('\n','');
	const decimalText = node.querySelector('.a-price .a-price-fraction').innerText
	return parseInt(wholeText) + parseFloat('0.' + decimalText)
}
function getImageSrc(node){
	const srcSetText = node.querySelector('span[data-component-type="s-product-image"] img').srcset
	
	const splitParts = srcSetText.split(",")
	const [src, x] = splitParts[splitParts.length - 1].split(" ")
	return src
}


function getData(node){
  
  return {
    sponsored: true,
    title: getTitle(node),
    rating: getRating(node),
    price: getPrice(node),
    prime: true,
    freeShipping: true,
    // temporarilyOutOfStock: true,
    imageSrc: getImageSrc(node),
    link: getLink(node),
    storeText: '',
    details: {
    },
    productId: '',
  }
}

function getCtrs(){
  return document.querySelectorAll('.s-card-container.s-overflow-hidden.aok-relative.s-include-content-margin.s-latency-cf-section.s-card-border')
}
function getLink(node){
  return node.querySelector('.a-link-normal.s-faceout-link.a-text-normal').href
}

function getMainData(i=0){
  const ctrs = getCtrs();
  const data = {}
  for (const node of ctrs){
    data['refrigerator'+i.toString()] = getData(node)
    i++;
  }
  return data

}
console.log(JSON.stringify(getMainData(93), null, 2));