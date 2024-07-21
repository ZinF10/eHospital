import { CATEGORIES_API, CURRENT_USER, TOKEN_API } from "@/redux/constants/constants";

const endpoints = {
    categories: CATEGORIES_API,
    token: TOKEN_API,
    current_user: CURRENT_USER,
    doctors: 'doctors/'
};

export default endpoints;