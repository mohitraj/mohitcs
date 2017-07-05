'''
In order to calculate linear regression 
y =a+bx

b = cov(x,y)/var(x)


'''

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class stats:

    def __init__(self):
        pass

    def get_data(self,file_name,*fields):
        data_list = []
        data = pd.read_csv(file_name)
        for each in fields:
            data_list.append(list(data.get(each)))
        return data_list

    def list_to_array(self,values):
        np_array = np.array(values)
        return np_array
    def get_mean(self,values):
        return np.mean(values)


    def get_std(self,values):
        return np.std(values)

    def variance(self,num_array):
        return np.var(num_array, ddof=1)

    def covariance(self,X_array,Y_array):
        return np.cov(X_array, Y_array)[0][1]

    def np_to_reg(self,array):
        length = len(array)
        return array.reshape((length, 1))

    def array_to_reg(self,array):
        np_array = self.list_to_array(array)
        return self.array_to_reg(np_array)


class Linear_Regression(stats):
    def __init__(self):
        pass

    def beta_coff(self,x_array,y_array):
        cov1 = self.covariance(x_array,y_array)
        var1 = self.variance(x_array)
        b= cov1/var1
        return b
    def intercept(self,x_array,y_array):
        x_mean = self.get_mean(x_array)
        y_mean = self.get_mean(y_array)
        beta = self.beta_coff(x_array,y_array)
        return y_mean- beta*x_mean

    def R_squared(self,x_tain,y_train,x_test,y_test):
        model = LinearRegression()
        x_tain = self.np_to_reg(x_tain)
        y_train = self.np_to_reg(y_train)

        x_test = self.np_to_reg(x_test)
        y_test = self.np_to_reg(y_test)
        model.fit(x_tain,y_train)
        return model.score(x_test, y_test)

    def predicted(self,x_train,y_train,x_test):
        model = LinearRegression()
        x_train = self.np_to_reg(x_train)
        y_train = self.np_to_reg(y_train)

        x_test = self.np_to_reg(x_test)
        model.fit(x_train, y_train)
        return  model.predict(x_test)

    def plot1(self,X_sc,Y_sc,x_data,y_data):
        plt.axis([0, 25, 0, 25])
        plt.grid(True)
        plt.scatter(X_sc, Y_sc)
        plt.plot(x_data,y_data, c='r', linestyle='--')
        plt.show()


obj1 = Linear_Regression()

X_values =[6, 8, 10, 14, 18]  # replace it
Y_values = [7, 9, 13, 17.5, 18]

X_test = [8,9,11,16,12]
Y_test = [11,8.5,15,18,11]




X_a = obj1.list_to_array(X_values)
Y_a = obj1.list_to_array(Y_values)

X_t = obj1.list_to_array(X_test)

'''
Y_t = obj1.list_to_array(Y_test)
print obj1.beta_coff(X_a,Y_a)
print obj1.intercept(X_a,Y_a)
print obj1.R_squared(X_a,Y_a, X_t,Y_t)
'''
y_pd=  obj1.predicted(X_a,Y_a, X_t)
print y_pd
print X_t
print obj1.plot1(X_a,Y_a,X_test,y_pd)

