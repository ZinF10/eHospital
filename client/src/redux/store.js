import AuthReducer from "./reducers/reducers";
import { configureStore } from '@reduxjs/toolkit';

export const store = configureStore({
    reducer: {
        user: AuthReducer,
    },
});