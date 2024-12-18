originalA =  [-1  1 -1 -1   1 0 0   8 ;
               2  4  0  0   0 1 0  10 ;
               0  0  1  1   0 0 1   3 ;
               2 -3  0 -5   0 0 0   0 ];
% originalA =  [-1  1 -1 -1   1 0 0   4 ;
%                2  4  0  0   0 1 0   5 ;
%                0  0  1  1   0 0 1   2 ;
%                2 -3  0 -5   0 0 0   0 ];
A = originalA;
Baze = [5, 6, 7];

function A = refactor_matrix(A, col, row)
    A(row, :) = A(row, :) / A(row, col); % normalizuojama eilutė "row"
    
    for r = [1:row-1, row+1:4]
        multiplier = -A(r, col); % daugiklis
            
        A(r, :) = A(r, :) + multiplier * A(row, :); % eliminuojama eilutė
    end
end

while true
    [min_cost, j] = min(A(end, 1:end-1));
    if min_cost >= 0 break; end

    RHS = A(1:end-1, end);
    A_j = A(1:end-1, j);
    A_j(A_j < 0) = 0; % paverst visus vardiklius, kurie < 0 į 0. 
    % tada dalinimas gražins Inf

    [lambda, leave_col_rowIndex] = min( RHS ./ A_j );
    Baze(leave_col_rowIndex) = j;

    A = refactor_matrix(A, j, leave_col_rowIndex);
end

Xfull = zeros(1,7);
Xfull(Baze) = A(1:3, end);
disp(Xfull(1:4));
disp("F(X) = 2*x1 − 3*x2 − 5*x4");
fprintf('X* = [%g, %g, %g, %g]\n',Xfull(1:4));
fprintf('F(X*) = 2*%g - 3*%g + 0*%g - 5*%g = %g',Xfull(1:4), -A(end, end));