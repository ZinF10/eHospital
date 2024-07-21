import { createContext, useContext } from 'react';
import AuthReducer from '@/redux/reducers/reducers';
import { useReducer } from 'react';
import cookie from 'react-cookies';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    let current = cookie.load('current_user');
    if (current === undefined) current = null;

    const [user, dispatch] = useReducer(AuthReducer, current);

    return (
        <AuthContext.Provider value={[user, dispatch]}>
            {children}
        </AuthContext.Provider>
    );
};

export const useCurrentUser = () => useContext(AuthContext);

export default AuthContext;