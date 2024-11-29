describe('Teste de Info Cultural - BANANA', () => {
    const userData = {
      username: "usuario_cultural",
      email: "cultural_user@example.com",
      password: "cultural123",
    };
  
    before(() => {
      // Configurações iniciais
      cy.exec('rm -f db.sqlite3'); // Para Windows; substitua por 'rm -f db.sqlite3' no Linux/Mac
      cy.exec('venv/bin/python manage.py migrate');
  
      // Cria um usuário no sistema
      cy.visit('http://127.0.0.1:8000/signup');
      cy.get('input[name="username"]').type(userData.username);
      cy.get('input[name="email"]').type(userData.email);
      cy.get('input[name="password1"]').type(userData.password);
      cy.get('input[name="password2"]').type(userData.password);
      cy.get('button[type="submit"]').click();
    });
  
    it('Usuário acessa informações culturais sobre Tomate', () => {
      // Login do usuário
      cy.visit('http://127.0.0.1:8000/login');
      cy.get('input[name="email"]').type(userData.email);
      cy.get('input[name="password"]').type(userData.password);
      cy.get('button[type="submit"]').click();
  
      // Acessar a página de informações culturais
      cy.visit('http://127.0.0.1:8000/infoculturas/');
  
      // Selecionar o botão "Mais informações" associado ao "BANANA"
      cy.contains('div', 'BANANA') // Localiza o container que contém o texto "BANANA"
        .parent() // Vai para o elemento pai do texto "TOMATE" (o cartão)
        .within(() => {
          cy.contains('Mais informações').click(); // Clica no botão dentro do cartão
        });
  
      // Verificar se as informações culturais sobre Banana são exibidas
      cy.url().should('include', 'http://127.0.0.1:8000/banana/'); // Verifica se está na URL correta
      cy.contains('Clima: Quentes, temperaturas entre 20°C e 30°C').should('be.visible'); // Verifica o título da página
    });
  });
  
