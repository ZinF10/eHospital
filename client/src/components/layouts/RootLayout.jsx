import { Outlet, useLocation } from 'react-router-dom';
import Footer from './Footer';
import Header from './Header';
import { PrivateRoutes, PublicRoutes } from '@/routes/routes';
import useDocumentTitle from '@/hooks/customs/useDocumentTitle';

const RootLayout = () => {
    const location = useLocation();
    const currentRoute = [...PublicRoutes, ...PrivateRoutes].find(route => route.path === location.pathname);
    const pageTitle = currentRoute ? `${currentRoute.title} - eHospital 🩺` : 'eHospital 🩺';
    useDocumentTitle(pageTitle)

    return (
        <>
            <Header />
            <main className='container'>
                <Outlet />
            </main>
            <Footer />
        </>
    );
};

export default RootLayout;