import Appointments from '@/pages/auth/Appointments';
import LogIn from '@/pages/auth/LogIn';
import Profile from '@/pages/auth/Profile';
import Register from '@/pages/auth/Register';
import About from '@/pages/core/About';
import Contact from '@/pages/core/Contact';
import Home from '@/pages/core/Home';
import PageNotFound from '@/pages/core/PageNotFound';

const PublicRoutes = [
    {
        path: '/',
        exact: true,
        component: Home,
        lazy: () => import('@/pages/core/Home'),
        title: 'Trang Chủ',
    },
    {
        path: '/about',
        component: About,
        lazy: () => import('@/pages/core/About'),
        title: 'Giới Thiệu',
    },
    {
        path: '/contact',
        component: Contact,
        lazy: () => import('@/pages/core/Contact'),
        title: 'Liên Hệ',
    },
    {
        path: '/login',
        component: LogIn,
        lazy: () => import('@/pages/auth/LogIn'),
        title: 'Đăng Nhập',
    },
    {
        path: '/register',
        component: Register,
        lazy: () => import('@/pages/auth/Register'),
        title: 'Đăng Kí',
    },
    {
        path: '*',
        component: PageNotFound,
        lazy: () => import('@/pages/core/PageNotFound'),
        title: '404 - Không Tìm Thấy',
    },
];

const PrivateRoutes = [
    {
        path: '/profile',
        component: Profile,
        lazy: () => import('@/pages/auth/Profile'),
        title: 'Hồ Sơ',
    },
    {
        path: '/appointments',
        component: Appointments,
        lazy: () => import('@/pages/auth/Appointments'),
        title: 'Cuộc Hẹn Của Tôi',
    },
];

export { PublicRoutes, PrivateRoutes }