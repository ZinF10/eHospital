import Avatar from '@/components/common/Avatar';
import { useCurrentUser } from '@/hooks/contexts/AuthContext';
import { formatFullName } from '@/utils/format';

const Profile = () => {
    const [user] = useCurrentUser();

    return (
        <section className='py-2'>
            <h3>Thông Tin Cá Nhân</h3>
            <Bio user={user} />
        </section>
    )
}

const Bio = ({ user }) => (
    <>
        <Avatar user={user} size={80} />
        <h5>{formatFullName(user.first_name, user.last_name)}</h5>
        <p>Email: {user.email}</p>
    </>
);


export default Profile