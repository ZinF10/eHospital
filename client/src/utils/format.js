const formatPrice = (price) => {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
    }).format(price);
};

const formatFullName = (firstName, lastName) => {
    return `${lastName} ${firstName}`
};


export { formatPrice, formatFullName }