import { useSelector } from 'react-redux'; 
import Post from '../Post';
import './index.css';

const Feed = () => {
    const posts = useSelector((state => state.postState.posts));
    
    const compare = (a, b) => {
        if (new Date(a.postDate) < new Date(b.postDate)) return 1;
        if (new Date(a.postDate) > new Date(b.postDate)) return -1;
        if (new Date(a.postDate) === new Date(b.postDate)) return 0;
    };
    
    return (
        <div className="feed-container">
            { posts && Object.values(posts).sort(compare).map( (post) => (
                <Post key={ post.id } postData={ post } />
                ))
            }
        </div>
)};

export default Feed;