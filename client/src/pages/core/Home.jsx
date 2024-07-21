import Greeting from "@/components/common/Greeting"
import ItemList from "@/components/common/ItemList"
import Loading from "@/components/common/Loading"
import NotFound from "@/components/common/NotFound"
import useAxios from "@/hooks/customs/useAxios"
import endpoints from "@/services/endpoints"

const Home = () => {
    const { data: doctors, isLoading } = useAxios(endpoints['doctors'])

    return (
        <div>
            <h2>Trang Chủ</h2>
            <Greeting />
            {
                isLoading ? (
                    <Loading />
                ) : doctors && doctors.length > 0 ? (
                    <ItemList doctors={doctors} />
                ) : (
                    <NotFound />
                )
            }
        </div>
    )
}

export default Home