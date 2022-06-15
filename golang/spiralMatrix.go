func spiralOrder(matrix [][]int) []int {
    var ans []int
    top, left := 0, 0
    colLength, rowLength := len(matrix), len(matrix[0])
    fmt.Println(rowLength * colLength)
    vector := "right"
    for len(ans) < (len(matrix) * len(matrix[0])) {

        switch vector {
            
        case "right":
            
            for i := left; i < rowLength; i++ {
                ans = append(ans, matrix[top][i])
            }
            top++
            vector = "down"

        case "down":
            
            for i := top; i < colLength; i++ {
                ans = append(ans, matrix[i][rowLength-1])
            }
            rowLength--
            vector = "left"

        case "left":
            
            for i := rowLength-1; i > left-1; i-- {
                ans = append(ans, matrix[colLength-1][i])
            }
            colLength--
            vector = "up"

        case "up":
            
            for i := colLength-1; i > top-1; i-- {
                ans = append(ans, matrix[i][left])
            }
            left++
            vector = "right"
        }

    }
    return ans
}
