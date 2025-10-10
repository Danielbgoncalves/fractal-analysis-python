function [d] = D(p)
    d=zeros(1,size(p,2));
    if(size(p,2)>1)
        r=zeros(1,size(p,2));
        for i=1:size(p,2);
            r(i)=3+(i*2-2);
        end
    else
        r=sqrt(size(p,1));
    end
    for i=1:size(p,2)
           d(i)=-(log(N(p(:,i)))/log(r(i)));
    end
end